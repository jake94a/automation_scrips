# fastapi expects this file to be called main.py

import fastapi
import git

app = fastapi.FastAPI()

@app.get('/')
def verify_message():
  return {'message': 'this works'}
  
@app.get('/git_update')
@app.post('/git_update')
def update():
  g = git.cmd.Git(path_to_thing_to_update)  # such as '~/jake-solo-react-challenge'
  g.pull()
  return {'message': 'repo pulled'}
