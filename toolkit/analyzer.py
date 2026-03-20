# toolkit/analyzer.py
"""
Handles:
1. summaries
2. filtering
3. counts
4. endpoint-specific analytics
"""

def summarize_posts(posts):
    unique_userId_set = {item.get('userId') for item in posts if item.get('userId') is not None}
    return {
        'total_posts': len(posts),
        'unique_users': len(unique_userId_set)
    }
        
def summarize_comments(comments):
    unique_emails = {item.get('email') for item in comments}
    return {
        'total_comments': len(comments),
        'unique_emails': len(unique_emails)
    }
def summarize_users(users):
    unique_companies_set = {item.get('company', {}).get('name') for item in users}
    
    return {
        "total_users": len(users),
        "unique_companies": len(unique_companies_set)
    }

def get_summary(endpoint, data):
    if endpoint == "posts":
        return summarize_posts(data)
    elif endpoint == "comments":
        return summarize_comments(data)
    elif endpoint == "users":
        return summarize_users(data)
    else:
        return {}