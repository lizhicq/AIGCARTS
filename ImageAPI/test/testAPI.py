import requests

# 设置API密钥
API_KEY = 'wAnuGRsDgloyh9l0LYskg49Gh_27wwUpNYgisX9GZn4'

def search_unsplash(query, page=1, per_page=10):
    """在Unsplash上搜索图片"""
    base_url = "https://api.unsplash.com/search/photos"
    headers = {
        "Authorization": f"Client-ID {API_KEY}"
    }
    params = {
        "query": query,
        "page": page,
        "per_page": per_page
    }
    response = requests.get(base_url, headers=headers, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

# 使用示例
if __name__ == "__main__":
    query = "mountains"
    results = search_unsplash(query)
    
    for photo in results['results']:
        print(photo['urls']['small'])
