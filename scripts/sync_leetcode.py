import os
import requests


LEETCODE_URL = "https://leetcode.com/graphql/"
USERNAME = "daviddavilad"

session = os.environ["LEETCODE_SESSION"]
csrf = os.environ["LEETCODE_CSRF_TOKEN"]

cookies = {
    "LEETCODE_SESSION": session,
    "csrftoken": csrf,
}

headers = {
    "Content-Type": "application/json",
    "Origin": "https://leetcode.com",
    "Referer": "https://leetcode.com/",
    "User-Agent": "Mozilla/5.0",
}


def graphql(query, variables):
    response.raise_for_status()

    data = response.json()

    print("GraphQL response:", data)

    if "errors" in data:
        raise RuntimeError(f"LeetCode GraphQL error: {data['errors']}")

    return data["data"]


def get_all_accepted_submissions():
    """
    Retrieve the authenticated user's submission history and
    return the latest accepted submission for each problem.
    """

    query = """
    query submissionList(
        $offset: Int!
        $limit: Int!
        $lastKey: String
    ) {
        submissionList(
            offset: $offset
            limit: $limit
            lastKey: $lastKey
        ) {
            lastKey
            hasNext
            submissions {
                id
                title
                titleSlug
                statusDisplay
                lang
                timestamp
            }
        }
    }
    """

    accepted = {}
    offset = 0
    last_key = None

    while True:
        print(f"Fetching submissions: offset={offset}")

        data = graphql(
            query,
            {
                "offset": offset,
                "limit": 20,
                "lastKey": last_key,
            },
        )

        result = data["submissionList"]

        submissions = result["submissions"]

        for submission in submissions:
            if submission["statusDisplay"] != "Accepted":
                continue

            slug = submission["titleSlug"]

            # Because we're walking newest -> oldest, the first
            # accepted submission we see for a problem is the latest.
            if slug not in accepted:
                accepted[slug] = submission

        if not result["hasNext"]:
            break

        offset += len(submissions)
        last_key = result["lastKey"]

        if not submissions:
            break

    return list(accepted.values())


def get_submission_code(submission_id):
    query = """
    query submissionDetails($submissionId: Int!) {
        submissionDetails(submissionId: $submissionId) {
            code
            lang {
                name
            }
        }
    }
    """

    data = graphql(
        query,
        {
            "submissionId": int(submission_id),
        },
    )

    return data["submissionDetails"]


def get_problem(slug):
    query = """
    query problem($titleSlug: String!) {
        question(titleSlug: $titleSlug) {
            questionFrontendId
            title
            titleSlug
        }
    }
    """

    data = graphql(
        query,
        {
            "titleSlug": slug,
        },
    )

    return data["question"]


def get_extension(language):
    extensions = {
        "python3": ".py",
        "python": ".py",
        "cpp": ".cpp",
        "c++": ".cpp",
        "java": ".java",
        "javascript": ".js",
        "typescript": ".ts",
        "c": ".c",
        "go": ".go",
        "rust": ".rs",
    }

    return extensions.get(language, ".txt")


def get_folder_name(problem):
    number = int(problem["questionFrontendId"])
    slug = problem["titleSlug"]

    return f"{number:04d}-{slug}"


# ---------------------------------------------------------
# Main
# ---------------------------------------------------------

submissions = get_all_accepted_submissions()

if submissions is None:
    raise RuntimeError(
        "LeetCode returned null for recentAcSubmissionList. "
        "This usually means the authentication/session is invalid "
        "or the GraphQL request is being rejected."
    )

print()
print(f"Found {len(submissions)} unique accepted problems.")

for submission in submissions:
    slug = submission["titleSlug"]

    problem = get_problem(slug)
    details = get_submission_code(submission["id"])

    folder = get_folder_name(problem)
    extension = get_extension(details["lang"]["name"])

    os.makedirs(folder, exist_ok=True)

    filename = f"solution{extension}"
    filepath = os.path.join(folder, filename)

    new_code = details["code"]

    if os.path.exists(filepath):
        with open(filepath, "r") as f:
            old_code = f.read()

        if old_code == new_code:
            print(f"Unchanged: {folder}/{filename}")
            continue

    with open(filepath, "w") as f:
        f.write(new_code)

    print(f"Updated: {folder}/{filename}")