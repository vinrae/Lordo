def approve_1():
    """Approve a pending change."""

    project = 'my-project'
    change_id = 'my-change'
    repo_name = 'my-repo'
    endpoint = 'https://www.example.com        project, repo_name, change_id)

    # Create a PullRequest object. The API expects the PullRequest to be
    # in the form of a JSON object, so we use the `dumps` function to
    # convert the PullRequest object to a JSON string.
    pull_request = {
        'status': 'APPROVED'
    }
    json_request = json.dumps(pull_request)

    # Make the request to the API.
    response = requests.put(
        endpoint,
        json=json_request,
        auth=get_auth())

    # Check if the request was successful.
    if response.status_code != 200:
        raise Exception('Status code: {}'.format(response.status_code))

    print('Approved change {}'.format(change_id))

