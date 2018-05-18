# from sqlalchemy.orm import sessionmaker
# from sqlalchemy import create_engine
# from models import Artist, Song
#
# engine = create_engine('sqlite:///artists.db', echo=True)
# Session = sessionmaker(bind=engine)
# session = Session()
#
# grateful_dead = Artist('Grateful Dead', 'rock', 53, 'San Francisco')
# kanye = Artist('Kanye West', 'hip hop', 40, 'Chicago')
#
# scarlet_begonias = Song('Scarlet Begonias', 320)
# good_life = Song('Good Life', 445)
#
# session.add(grateful_dead)
# session.add(kanye)
# session.add(scarlet_begonias)
# session.add(good_life)
# session.commit()
#
# import pdb; pdb.set_trace()
