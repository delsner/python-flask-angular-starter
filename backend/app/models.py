from sqlalchemy.dialects.postgresql import JSONB

from app import db


class Cluster(db.Model):
    """This class represents the cluster table."""

    __tablename__ = 'clusters'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(
        db.DateTime, default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())
    data = db.Column(JSONB)

    def __init__(self, name, data):
        """initialize with name."""
        self.name = name
        self.data = data

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Cluster.query.all()

    @staticmethod
    def get_single(id):
        return Cluster.query.filter_by(id=id).first()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<Cluster: {}>".format(self.name)
