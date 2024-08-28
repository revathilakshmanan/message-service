from uuid import uuid4
from sqlalchemy import Column, String
from app import db

class Message(db.Model):
    __tablename__ = 'messages'

    account_id = Column(String, nullable=False)
    message_id = Column(String, primary_key=True, default=lambda: str(uuid4()))
    sender_number = Column(String, nullable=False)
    receiver_number = Column(String, nullable=False)

    def to_dict(self):
        return {
            "account_id": self.account_id,
            "message_id": self.message_id,
            "sender_number": self.sender_number,
            "receiver_number": self.receiver_number
        }



