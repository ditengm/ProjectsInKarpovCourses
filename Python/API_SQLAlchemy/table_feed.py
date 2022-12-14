from sqlalchemy import Column, Integer, String, func, ForeignKey, DATETIME
from sqlalchemy.orm import relationship

from database import Base, SessionLocal


class Feed(Base):
    __tablename__ = 'feed_action'
    user_id = Column(Integer, ForeignKey("user.id"), primary_key=True)
    user = relationship("User")
    post_id = Column(Integer, ForeignKey("post.id"), primary_key=True)
    post = relationship("Post")
    action = Column(String)
    time = Column(DATETIME)

