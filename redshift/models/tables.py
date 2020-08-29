import sqlalchemy as sa

from redshift.models.base import Base


class Users(Base):
    __tablename__ = 'users'

    userid = sa.Column(sa.Integer, primary_key=True)
    username = sa.Column(sa.CHAR(length=8))
    firstname = sa.Column(sa.VARCHAR(length=30))
    lastname = sa.Column(sa.VARCHAR(length=30))
    city = sa.Column(sa.VARCHAR(length=30))
    state = sa.Column(sa.CHAR(length=2))
    email = sa.Column(sa.VARCHAR(length=100))
    phone = sa.Column(sa.CHAR(length=14))
    likesports = sa.Column(sa.Boolean)
    liketheatre = sa.Column(sa.Boolean)
    likeconcerts = sa.Column(sa.Boolean)
    likejazz = sa.Column(sa.Boolean)
    likeclassical = sa.Column(sa.Boolean)
    likeopera = sa.Column(sa.Boolean)
    likerock = sa.Column(sa.Boolean)
    likevegas = sa.Column(sa.Boolean)
    likebroadway = sa.Column(sa.Boolean)
    likemusicals = sa.Column(sa.Boolean)

    __table_args__ = {
        'redshift_sortkey': 'userid',
        'redshift_distkey': 'userid',
    }

    def __init__(
        self,
        userid: int,
        username: str,
        firstname: str,
        lastname: str,
        city: str,
        state: str,
        email: str,
        phone: str,
        likesports: bool,
        liketheatre: bool,
        likeconcerts: bool,
        likejazz: bool,
        likeclassical: bool,
        likeopera: bool,
        likerock: bool,
        likevegas: bool,
        likebroadway: bool,
        likemusicals: bool,
    ):
        self.userid = userid
        self.username = username
        self.firstname = firstname
        self.lastname = lastname
        self.city = city
        self.state = state
        self.email = email
        self.phone = phone
        self.likesports = likesports
        self.liketheatre = liketheatre
        self.likeconcerts = likeconcerts
        self.likejazz = likejazz
        self.likeclassical = likeclassical
        self.likeopera = likeopera
        self.likerock = likerock
        self.likevegas = likevegas
        self.likebroadway = likebroadway
        self.likemusicals = likemusicals
