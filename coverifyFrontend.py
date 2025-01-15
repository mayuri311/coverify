from nicegui import ui
from nicegui.events import ValueChangeEventArguments
from urllib.request import urlopen
import urllib.request
import json

from ui import show

ui.html('Enter your <strong>tender id</strong>')

spotifyID = ""
playlistNameID = {}
playlists = {}
playlistID = ''
selectedPlaylist = ""
image_jsonResponse = ''


def handle_input(e):
    global spotifyID
    spotifyID = e.value


def retrievePlaylists():
    s_url = "http://127.0.0.1:8000/coverify/getPlaylists/"
    response = urlopen(s_url)
    pl_data = json.loads(response.read())
    # print("playlists", pl_data)
    global playlistNameID
    playlistNameID["name"] = []
    playlistNameID["id"] = []
    for playlist in pl_data:
        # print(playlist)
        playlistNameID["name"].append(playlist["name"])
        playlistNameID["id"].append(playlist["id"])
    # print("list of playlists from retrieve playlists", playlistNameID)
    return playlistNameID


def registerUserid():
    s_url = "http://127.0.0.1:8000/coverify/setUserID/" + str(spotifyID)
    response = urlopen(s_url)
    data = json.loads(response.read())
    # read the data from the URL and print it
    # print(data)
    global playlists
    playlists = retrievePlaylists()


def registerSelection(event: ValueChangeEventArguments):
    global selectedPlaylist
    global playlistID
    selectedPlaylist = event.value
    index = playlists["name"].index(selectedPlaylist)
    playlistID = playlists["id"][int(index)]
    s_url = "http://127.0.0.1:8000/coverify/setPlaylist/{playlist}?playlistID=" + str(playlistID)
    print(s_url)
    response = urlopen(s_url)
    print("register selection", selectedPlaylist, playlistID, index, s_url)


def generateImage():
    s_url = "http://127.0.0.1:8000/coverify/getImageURL/"
    response = urlopen(s_url)
    global image_jsonResponse
    image_jsonResponse = json.loads(response.read())
    return image_jsonResponse


def switchToPlaylistPage():
    registerUserid()
    ui.navigate.to('/playlists')


def switchToImagePage():
    ui.navigate.to('/image')



@ui.page('/', response_timeout=999)
@ui.page('/home', response_timeout=999)
def show_home():
    with ui.column().classes('w-full items-center'):
        with ui.row().classes('w-full justify-center'):
            ui.image('https://i.ibb.co/mX99VQx/image.png').props(f"width={250}px height={110}px")
        with ui.row().classes('w-full justify-center'):
            ui.input(placeholder='Enter Spotify ID', on_change=handle_input)
            ui.button(text='→', on_click=switchToPlaylistPage, color='#10b981')



@ui.page('/playlists', response_timeout=999)
def show_playlists():
    with ui.column().classes('w-full items-center'):
        if playlists:
            ui.image('https://i.ibb.co/DrH9fgJ/Screenshot-2024-07-20-at-8-50-52-AM.png').props(f"width={260}px height={73}px")
            with ui.row():
                ui.select(options=playlists["name"], value=playlists["name"][0], on_change=registerSelection)
                ui.button(text='LOAD', on_click=switchToImagePage, color='#10b981')

@ui.page('/image', response_timeout=999)
def show_image():
    with ui.column().classes('w-full items-center'):

        ui.image('https://i.ibb.co/mX99VQx/image.png').props(f"width={250}px height={110}px")
        image_url = generateImage()
        ui.image(image_url["image url"]).classes('w-96 drop-shadow-md rounded')
        with ui.row():
            ui.button(text='←', on_click=switchToPlaylistPage, color='#10b981')
            ui.button(text='REGENERATE', on_click=switchToImagePage, color='#10b981')




ui.run(port=5001)
