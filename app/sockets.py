import socketio
import aioredis
import json
from fastapi import FastAPI, Request

sio_server = socketio.AsyncServer(
    async_mode='asgi',
    cors_allowed_origins=[]
)

sio_app = socketio.ASGIApp(
    socketio_server=sio_server,
    socketio_path='sockets'
)

@sio_server.event
async def connect(sid, environ, auth):
    print(f'{sid}: connected')
    await sio_server.emit('join', {'sid': sid})


@sio_server.event
async def chat(sid, message):
    await sio_server.emit('chat', {'sid': sid, 'message': message})


@sio_server.event
async def disconnect(sid):
    print(f'{sid}: disconnected')


@sio_server.event
async def message(sid, data):
    await sio_server.emit("message", data, room=sid)


@sio_server.on('join')
async def ping_message(sid, data):
    print(data)
    await sio_server.emit("join", 'hello!~~ from server', room=sid)


# import socketio

# # create a Socket.IO server
# sio_server = socketio.Server()

# # wrap with a WSGI application
# sio_app = socketio.WSGIApp(sio_server)


# @sio_server.event
# def connect(sid, environ, auth):
#     print(f'{sid}: connected')
#     sio_server.emit('join', {'sid': sid})


# @sio_server.event
# def chat(sid, message):
#     sio_server.emit('chat', {'sid': sid, 'message': message})


# @sio_server.event
# def disconnect(sid):
#     print(f'{sid}: disconnected')


# @sio_server.event
# async def message(sid, data):
#     await sio_server.emit("message", data, room=sid)


# @sio_server.on('join')
# def ping_message(sid, data):
#     print(data)
#     sio_server.emit("join", 'hello!~~ from server', room=sid)