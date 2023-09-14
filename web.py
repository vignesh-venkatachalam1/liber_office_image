from fastapi import FastAPI,Request
import uvicorn

app=FastAPI(title='demo',description='demo des')

@app.post('/hello')
def helloIndex():
    return 'hello world'

if __name__=='__main__':
    uvicorn.run(app,host='0.0.0.0',port=9001,reload=False)

