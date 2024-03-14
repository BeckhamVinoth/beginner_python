import subprocess


def generate_change_log():
    # Get the commit messages from the Git repository
    git_log_command = ['git', 'log', '--pretty=format:%s']
    commit_messages = subprocess.check_output(git_log_command, universal_newlines=True)
    commit_messages = commit_messages.strip().split('\n')

    # Format commit messages into Markdown change log entries
    change_log_entries = []
    for message in commit_messages:
        change_log_entry = f"* {message}"
        change_log_entries.append(change_log_entry)

    # Write change log entries to a file
    with open('CHANGELOG.md', 'w') as changelog_file:
        changelog_file.write("# Change Log\n\n")
        changelog_file.write("\n".join(change_log_entries))


if __name__ == "__main__":
    generate_change_log()
