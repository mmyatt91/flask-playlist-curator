"""Forms for playlist app."""

from wtforms import SelectField, TextAreaField, StringField
from wtforms.validators import InputRequired, Length, NumberRange, Email, Optional
from flask_wtf import FlaskForm


class PlaylistForm(FlaskForm):
    """Form for adding playlists."""

    # Add the necessary code to use this form
    name = StringField(
        "Playlist Name",
        validators=[InputRequired(), Length(min=1, max=50)],
    )

    description = TextAreaField(
        "Description",
        validators=[Optional()],
    )


class SongForm(FlaskForm):
    """Form for adding songs."""

    # Add the necessary code to use this form
    title = TextAreaField(
        "Song Title",
        validators=[InputRequired()],
    ) 
    
    artist = StringField(
        "Artist Name",
        validators=[InputRequired(), Length(min=1, max=50)],
    )


# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE
class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add', coerce=int)
