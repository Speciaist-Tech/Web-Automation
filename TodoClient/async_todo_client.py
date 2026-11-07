class AsyncTodoClient:
    def __init__(self):
        self.client = httpx.AsyncClient(base_url="https://jsonplaceholder.typicode.com",headers={"name":"Cypher"}, timeout=10)


    async def _request(self, method, path, **kwargs):
        try:
            response = await self.client.request(method, path, **kwargs)
            response.raise_for_status()
            return response
        
        except httpx.HTTPStatusError as e:
            print(f"HttpStatusError: {e}")
            return None

        except httpx.RequestError as re:
            print(f"RequestError: {re}")
            return None
    
    async def get_todo(self, todo_id):
        response = await self._request("GET", f"/todos/{todo_id}")
        if response is None:
            return None
        return response.json()

    async def list_todos(self, user_id=None):
        if user_id:
            get_req = await self._request("GET", "/todos", params={"userId":user_id})
        else:
            get_req = await self._request("GET", "/todos", params={})

        if get_req is None:
            return None
        return get_req.json()

    async def create_post(self, title, body, user_id=1):
        post_req = await self._request("POST", "/posts", json={"title":title, "body":body, "userId": user_id})
        if post_req is None:
            return None
        return post_req.json()
        
    async def close(self):
        await self.client.aclose()
