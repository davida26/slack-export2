<<<<<<< HEAD
import flask


app = flask.Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)


@app.route("/channel/<name>/")
def channel_name(name):
    messages = flask._app_ctx_stack.channels[name]
    channels = list(flask._app_ctx_stack.channels.keys())
    groups = list(flask._app_ctx_stack.groups.keys())
    dm_users = list(flask._app_ctx_stack.dm_users)
    mpim_users = list(flask._app_ctx_stack.mpim_users)

    return flask.render_template("viewer.html", messages=messages,
                                 name=name.format(name=name),
                                 channels=sorted(channels),
                                 groups=sorted(groups),
                                 dm_users=dm_users,
                                 mpim_users=mpim_users)

@app.route("/group/<name>/")
def group_name(name):
    messages = flask._app_ctx_stack.groups[name]
    channels = list(flask._app_ctx_stack.channels.keys())
    groups = list(flask._app_ctx_stack.groups.keys())
    dm_users = list(flask._app_ctx_stack.dm_users)
    mpim_users = list(flask._app_ctx_stack.mpim_users)

    return flask.render_template("viewer.html", messages=messages,
                                 name=name.format(name=name),
                                 channels=sorted(channels),
                                 groups=sorted(groups),
                                 dm_users=dm_users,
                                 mpim_users=mpim_users)


@app.route("/dm/<id>/")
def dm_id(id):
    messages = flask._app_ctx_stack.dms[id]
    channels = list(flask._app_ctx_stack.channels.keys())
    groups = list(flask._app_ctx_stack.groups.keys())
    dm_users = list(flask._app_ctx_stack.dm_users)
    mpim_users = list(flask._app_ctx_stack.mpim_users)

    return flask.render_template("viewer.html", messages=messages,
                                 id=id.format(id=id),
                                 channels=sorted(channels),
                                 groups=sorted(groups),
                                 dm_users=dm_users,
                                 mpim_users=mpim_users)


@app.route("/mpim/<name>/")
def mpim_name(name):
    messages = flask._app_ctx_stack.mpims[name]
    channels = list(flask._app_ctx_stack.channels.keys())
    groups = list(flask._app_ctx_stack.groups.keys())
    dm_users = list(flask._app_ctx_stack.dm_users)
    mpim_users = list(flask._app_ctx_stack.mpim_users)

    return flask.render_template("viewer.html", messages=messages,
                                 name=name.format(name=name),
                                 channels=sorted(channels),
                                 groups=sorted(groups),
                                 dm_users=dm_users,
                                 mpim_users=mpim_users)


@app.route("/")
def index():
    channels = list(flask._app_ctx_stack.channels.keys())
    # return flask.render_template("home.html")
    if "general" in channels:
        return channel_name("general")
    else:
        return channel_name(channels[0])

@app.route("/dashboard")
def dashboard():
    channels = list(flask._app_ctx_stack.channels.keys())
    groups = list(flask._app_ctx_stack.groups.keys())
    dm_users = list(flask._app_ctx_stack.dm_users)
    mpim_users = list(flask._app_ctx_stack.mpim_users)
    
    return flask.render_template("home.html", channels=sorted(channels),
                                groups=sorted(groups),
                                dm_users=dm_users,
                                mpim_users=mpim_users)

=======
#!/usr/bin/env python

from slackviewer.main import main

if __name__ == '__main__':
    main()
>>>>>>> b94a59185650b8a3ae389938a014cd10d5612e66
