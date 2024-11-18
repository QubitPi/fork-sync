from git import Repo

def get_repo_name_from_url(url: str) -> str:
    """
    Credits to https://stackoverflow.com/a/55137835
    """
    last_slash_index = url.rfind("/")
    last_suffix_index = url.rfind(".git")
    if last_suffix_index < 0:
        last_suffix_index = len(url)

    if last_slash_index < 0 or last_suffix_index <= last_slash_index:
        raise Exception("Badly formatted url {}".format(url))

    return url[last_slash_index + 1:last_suffix_index]

if __name__ == "__main__":

    urls = [
        ("git@github.com:QubitPi/MiniSearch.git", "git@github.com:felladrin/MiniSearch.git"),
        ("git@github.com:QubitPi/docs.konghq.com.git", "git@github.com:Kong/docs.konghq.com.git"),
        ("git@github.com:QubitPi/docker-kong.git", "git@github.com:Kong/docker-kong.git"),
        ("git@github.com:QubitPi/mlflow.git", "git@github.com:mlflow/mlflow.git"),
        ("git@github.com:QubitPi/elastic-docs.git", "git@github.com:elastic/docs.git"),
        ("git@github.com:QubitPi/logstash-docs.git", "git@github.com:elastic/logstash-docs.git"),
        ("git@github.com:QubitPi/logstash.git", "git@github.com:QubitPi/logstash.git"),
        ("git@github.com:QubitPi/docker-docs.git", "git@github.com:docker/docs.git"),
        ("git@github.com:QubitPi/docker-install.git", "git@github.com:docker/docker-install.git"),
    ]

    for repo_url in urls:
        forked_repo = repo_url[0]
        upstream_repo = repo_url[1]

        repo = Repo.clone_from(forked_repo, "../daily-sync/{}".format(get_repo_name_from_url(forked_repo)))
        repo.create_remote("upstream", upstream_repo) # https://gitpython.readthedocs.io/en/stable/tutorial.html#handling-remotes
