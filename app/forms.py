from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SelectMultipleField, DateTimeField, BooleanField
from wtforms.validators import DataRequired, AnyOf, URL, Length, Regexp

class ShowForm(FlaskForm):
    artist_id = StringField(
        'artist_id',  validators=[DataRequired()]
    )
    venue_id = StringField(
        'venue_id',  validators=[DataRequired()]
    )
    start_time = DateTimeField(
        'start_time',
        validators=[DataRequired()],
        default= datetime.today()
    )

class VenueForm(FlaskForm):
    name = StringField(
        'name', validators=[DataRequired(), Length(max=100)]
    )
    city = StringField(
        'city', validators=[DataRequired(), Length(max=35)]
    )
    state = SelectField(
        'state', validators=[DataRequired()],
        choices=[
            ('AL', 'AL'),
            ('AK', 'AK'),
            ('AZ', 'AZ'),
            ('AR', 'AR'),
            ('CA', 'CA'),
            ('CO', 'CO'),
            ('CT', 'CT'),
            ('DE', 'DE'),
            ('DC', 'DC'),
            ('FL', 'FL'),
            ('GA', 'GA'),
            ('HI', 'HI'),
            ('ID', 'ID'),
            ('IL', 'IL'),
            ('IN', 'IN'),
            ('IA', 'IA'),
            ('KS', 'KS'),
            ('KY', 'KY'),
            ('LA', 'LA'),
            ('ME', 'ME'),
            ('MT', 'MT'),
            ('NE', 'NE'),
            ('NV', 'NV'),
            ('NH', 'NH'),
            ('NJ', 'NJ'),
            ('NM', 'NM'),
            ('NY', 'NY'),
            ('NC', 'NC'),
            ('ND', 'ND'),
            ('OH', 'OH'),
            ('OK', 'OK'),
            ('OR', 'OR'),
            ('MD', 'MD'),
            ('MA', 'MA'),
            ('MI', 'MI'),
            ('MN', 'MN'),
            ('MS', 'MS'),
            ('MO', 'MO'),
            ('PA', 'PA'),
            ('RI', 'RI'),
            ('SC', 'SC'),
            ('SD', 'SD'),
            ('TN', 'TN'),
            ('TX', 'TX'),
            ('UT', 'UT'),
            ('VT', 'VT'),
            ('VA', 'VA'),
            ('WA', 'WA'),
            ('WV', 'WV'),
            ('WI', 'WI'),
            ('WY', 'WY'),
        ]
    )
    address = StringField(
        'address', validators=[DataRequired()]
    )
    phone = StringField(
        'phone', validators=[Regexp('^\d{3}-\d{3}-\d{4}$', message="Phone number must be in format: xxx-xxx-xxxx")]
    )
    image = StringField(
        'image', validators=[URL()]
    )
    genres = SelectMultipleField(
        'genres', validators=[DataRequired()],
        choices=[
            ('Alternative', 'Alternative'),
            ('Blues', 'Blues'),
            ('Classical', 'Classical'),
            ('Country', 'Country'),
            ('Electronic', 'Electronic'),
            ('Folk', 'Folk'),
            ('Funk', 'Funk'),
            ('Hip-Hop', 'Hip-Hop'),
            ('Heavy Metal', 'Heavy Metal'),
            ('Instrumental', 'Instrumental'),
            ('Jazz', 'Jazz'),
            ('Musical Theatre', 'Musical Theatre'),
            ('Pop', 'Pop'),
            ('Punk', 'Punk'),
            ('R&B', 'R&B'),
            ('Reggae', 'Reggae'),
            ('Rock n Roll', 'Rock n Roll'),
            ('Soul', 'Soul'),
            ('Other', 'Other'),
        ]
    )
    facebook = StringField(
        'facebook', validators=[URL()]
    )
    site = StringField(
        'site', validators=[URL()]
    )

    seeking_talent = BooleanField( 'seeking_talent' )

    seeking_description = StringField(
        'seeking_description'
    )



class ArtistForm(FlaskForm):
    name = StringField(
        'name', validators=[DataRequired(), Length(max=100)]
    )
    city = StringField(
        'city', validators=[DataRequired(), Length(max=35)]
    )
    state = SelectField(
        'state', validators=[DataRequired()],
        choices=[
            ('AL', 'AL'),
            ('AK', 'AK'),
            ('AZ', 'AZ'),
            ('AR', 'AR'),
            ('CA', 'CA'),
            ('CO', 'CO'),
            ('CT', 'CT'),
            ('DE', 'DE'),
            ('DC', 'DC'),
            ('FL', 'FL'),
            ('GA', 'GA'),
            ('HI', 'HI'),
            ('ID', 'ID'),
            ('IL', 'IL'),
            ('IN', 'IN'),
            ('IA', 'IA'),
            ('KS', 'KS'),
            ('KY', 'KY'),
            ('LA', 'LA'),
            ('ME', 'ME'),
            ('MT', 'MT'),
            ('NE', 'NE'),
            ('NV', 'NV'),
            ('NH', 'NH'),
            ('NJ', 'NJ'),
            ('NM', 'NM'),
            ('NY', 'NY'),
            ('NC', 'NC'),
            ('ND', 'ND'),
            ('OH', 'OH'),
            ('OK', 'OK'),
            ('OR', 'OR'),
            ('MD', 'MD'),
            ('MA', 'MA'),
            ('MI', 'MI'),
            ('MN', 'MN'),
            ('MS', 'MS'),
            ('MO', 'MO'),
            ('PA', 'PA'),
            ('RI', 'RI'),
            ('SC', 'SC'),
            ('SD', 'SD'),
            ('TN', 'TN'),
            ('TX', 'TX'),
            ('UT', 'UT'),
            ('VT', 'VT'),
            ('VA', 'VA'),
            ('WA', 'WA'),
            ('WV', 'WV'),
            ('WI', 'WI'),
            ('WY', 'WY'),
        ]
    )
    phone = StringField(
        'phone', validators=[Regexp('^\d{3}-\d{3}-\d{4}$', message="Phone number must be in format: xxx-xxx-xxxx")]
    )
    image = StringField(
        'image'
    )
    genres = SelectMultipleField(
        'genres', validators=[DataRequired()],
        choices=[
            ('Alternative', 'Alternative'),
            ('Blues', 'Blues'),
            ('Classical', 'Classical'),
            ('Country', 'Country'),
            ('Electronic', 'Electronic'),
            ('Folk', 'Folk'),
            ('Funk', 'Funk'),
            ('Hip-Hop', 'Hip-Hop'),
            ('Heavy Metal', 'Heavy Metal'),
            ('Instrumental', 'Instrumental'),
            ('Jazz', 'Jazz'),
            ('Musical Theatre', 'Musical Theatre'),
            ('Pop', 'Pop'),
            ('Punk', 'Punk'),
            ('R&B', 'R&B'),
            ('Reggae', 'Reggae'),
            ('Rock n Roll', 'Rock n Roll'),
            ('Soul', 'Soul'),
            ('Other', 'Other'),
        ]
     )
    facebook = StringField(
        # TODO implement enum restriction
        'facebook', validators=[URL()]
     )

    site = StringField(
        'site', validators=[URL()]
     )

    seeking_venue = BooleanField( 'seeking_venue' )

    seeking_description = StringField(
            'seeking_description'
     )

