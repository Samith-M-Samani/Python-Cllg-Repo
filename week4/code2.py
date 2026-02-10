# 2. Filter Valid Email Domains

# Problem Statement
# You are given a list of email addresses. Return a list of usernames (part before @) whose email domain belongs to a given set of allowed domains.

# Input

# emails = ["alice@gmail.com", "bob@yahoo.com", "carol@gmail.com"]
# allowed_domains = {"gmail.com"}


# Output

# ["alice", "carol"]


# Constraints

# Use filter() to validate domains

# Use map() to extract usernames

def filter_valid_email_domains(emails, allowed_domains):
    
    valid_emails = list(filter(lambda email: email.split('@')[1] in allowed_domains, emails))
    
    
    usernames = list(map(lambda email: email.split('@')[0], valid_emails))
    
    return usernames