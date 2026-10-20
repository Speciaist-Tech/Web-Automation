class TodoClient:
    def __init__(self):
        self.client = httpx.Client(base_url="https://jsonplaceholder.typicode.com",headers={"name":"Cypher"}, timeout=10)


    def _request(self, method, path, **kwargs):
        try:
            response = self.client.request(method, path, **kwargs)
            response.raise_for_status()
            return response
        
        except httpx.HTTPStatusError as e:
            print(f"HttpStatusError: {e}")
            return None

        except httpx.RequestError as re:
            print(f"RequestError: {re}")
            return None
    
    def get_todo(self, todo_id):
        _request = self._request("GET", f"/todos/{todo_id}")
        if _request is None:
            return None
        else:
            print(_request.status_code)
            print(_request.json())

    def list_todos(self, user_id=None):
        if user_id:
            get_req = self._request("GET", "/todos", params={"userId":user_id})
        else:
            get_req = self._request("GET", "/todos", params={})

        if get_req is None:
            return None
        return get_req.json()

    def create_post(self, title, body, user_id=1):
        post_req = self._request("POST", "/posts", json={"title":title, "body":body, "userId": user_id})
        if post_req is None:
            return None
        return post_req.json()
        
    def close(self):
        self.client.close()
