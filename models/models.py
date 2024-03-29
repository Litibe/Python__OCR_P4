from LANGUAGES import french as language
from utils import constants

from sqlalchemy import Column, Integer, Float, \
    String, ForeignKey, Date, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# Base class used by my classes (my entities)
Base = declarative_base()  # Required for SQLAlchemy


class Players(Base):
    __tablename__ = "T_Players"
    player_id = Column(Integer, primary_key=True, autoincrement=True)
    last_name = Column(String)
    first_name = Column(String)
    birthday = Column(Date)
    sex = Column(String)
    rank = Column(Integer)
    pts_rank = Column(Float)
    pts_tournament = Column(Float)
    adversary_tournament = Column(String)

    def __init__(self, last_name, first_name, birthday, sex, rank):
        self.last_name = last_name
        self.first_name = first_name
        self.birthday = birthday
        self.sex = sex
        self.rank = rank
        self.pts_rank = 0

    def __str__(self):
        if self.pts_tournament is None:
            self.pts_matchs = ""
        else:
            self.pts_matchs = f"{language.STR_PLAYER_PTS_TOURNAMENT} " \
                              f"{self.pts_tournament} "\
                              f"{language.STR_PLAYER_PTS_TOURNAMENT2}"
        return f"{language.STR_PLAYER_1}{self.player_id} - {self.last_name} " \
               f"{self.first_name} - " \
               f"{self.birthday.strftime('%d/%m/%Y')} - " \
               f"{language.STR_PLAYER_3}" \
               f"{self.sex} - {language.STR_PLAYER_RANK} " \
               f"{self.rank} {language.STR_PLAYER_RANK2} - " \
               f"{language.STR_PLAYER_PTS_TOURNAMENT} " \
               f"{self.pts_rank} "\
               f"{language.STR_PLAYER_PTS} " \
               f"{language.STR_PLAYER_RANK2} - " \
               f"{self.pts_matchs}"

    def watch_pts_tournament(self):
        return f"{self.last_name} {self.first_name} " \
               f"{language.STR_PLAYER_PTS_TOURNAMENT} " \
               f"{self.pts}"


class Match(Base):
    __tablename__ = "T_Match"
    match_id = Column(Integer, primary_key=True, autoincrement=True)
    id_player1 = Column(Integer, ForeignKey("T_Players.player_id"))
    player_1 = relationship('Players', foreign_keys="Match.id_player1")
    result_player_1 = Column(Float)
    id_player2 = Column(Integer, ForeignKey("T_Players.player_id"))
    player_2 = relationship('Players', foreign_keys="Match.id_player2")
    result_player_2 = Column(Float)

    def __init__(self,
                 id_player1, result_player_1,
                 id_player2, result_player_2
                 ):
        self.id_player1 = id_player1
        self.result_player_1 = result_player_1
        self.id_player2 = id_player2
        self.result_player_2 = result_player_2

    def __str__(self):
        return f"Player ID N°{self.player_1.player_id} " \
               f" {self.player_1.last_name} {self.player_1.first_name} " \
               f"{language.STR_SCORE} {self.result_player_1} " \
               f"{language.STR_SCORE2} \n" \
               f"Player ID N°{self.player_2.player_id} " \
               f" {self.player_2.last_name} {self.player_2.first_name} " \
               f"{language.STR_SCORE} {self.result_player_2} " \
               f"{language.STR_SCORE2}"


class Rounds(Base):
    __tablename__ = "T_Rounds"
    round_id = Column(Integer, primary_key=True, autoincrement=True)
    link_tournament_id = Column(Integer, ForeignKey(
        "T_Tournament.tournament_id"))
    name_round = Column(String)
    tournament_details = relationship(
        "Tournament", foreign_keys="Rounds.link_tournament_id")
    date_started = Column(DateTime)
    date_finished = Column(DateTime, nullable=True)

    match1_id = Column(Integer, ForeignKey("T_Match.match_id"))
    match1_details = relationship("Match", foreign_keys="Rounds.match1_id")
    match2_id = Column(Integer, ForeignKey("T_Match.match_id"))
    match2_details = relationship("Match", foreign_keys="Rounds.match2_id")
    match3_id = Column(Integer, ForeignKey("T_Match.match_id"))
    match3_details = relationship("Match", foreign_keys="Rounds.match3_id")
    match4_id = Column(Integer, ForeignKey("T_Match.match_id"))
    match4_details = relationship("Match", foreign_keys="Rounds.match4_id")

    def __init__(self, name_round, date):
        self.name_round = name_round
        self.date_started = date

    def __str__(self):
        return f"----------------------------------------\n" \
               f"{language.STR_ROUNDS_1} {self.round_id} \n" \
               f"{self.name_round}" \
               f"\n {language.STR_ROUND_STARTED} " \
               f"{self.date_started.strftime('%d/%m/%Y %H:%M:%S')} " \
               f"\n----------------------------------------\n"\
               f"\nMatch1 ID N°{self.match1_id} : " \
               f"\n{self.match1_details}" \
               f"\n----------------------------------------\n"\
               f"\nMatch2 ID N°{self.match2_id} : " \
               f"\n{self.match2_details}" \
               f"\n----------------------------------------\n"\
               f"\nMatch3 ID N°{self.match3_id} : " \
               f"\n{self.match3_details}" \
               f"\n----------------------------------------\n"\
               f"\nMatch4 ID N°{self.match4_id} : " \
               f"\n{self.match4_details}" \
               f"\n"\
               f"\n{language.STR_ROUND_FINISHED} " \
               f"{self.date_finished.strftime('%d/%m/%Y %H:%M:%S')} \n"


class PlayersForTournament(Base):
    __tablename__ = "T_PlayersForTournament"
    players_tournament_id = Column(
        Integer, primary_key=True, autoincrement=True)
    id_player1 = Column(Integer, ForeignKey("T_Players.player_id"))
    player_1 = relationship(
        'Players', foreign_keys="PlayersForTournament.id_player1")
    id_player2 = Column(Integer, ForeignKey("T_Players.player_id"))
    player_2 = relationship(
        'Players', foreign_keys="PlayersForTournament.id_player2")
    id_player3 = Column(Integer, ForeignKey("T_Players.player_id"))
    player_3 = relationship(
        'Players', foreign_keys="PlayersForTournament.id_player3")
    id_player4 = Column(Integer, ForeignKey("T_Players.player_id"))
    player_4 = relationship(
        'Players', foreign_keys="PlayersForTournament.id_player4")
    id_player5 = Column(Integer, ForeignKey("T_Players.player_id"))
    player_5 = relationship(
        'Players', foreign_keys="PlayersForTournament.id_player5")
    id_player6 = Column(Integer, ForeignKey("T_Players.player_id"))
    player_6 = relationship(
        'Players', foreign_keys="PlayersForTournament.id_player6")
    id_player7 = Column(Integer, ForeignKey("T_Players.player_id"))
    player_7 = relationship(
        'Players', foreign_keys="PlayersForTournament.id_player7")
    id_player8 = Column(Integer, ForeignKey("T_Players.player_id"))
    player_8 = relationship(
        'Players', foreign_keys="PlayersForTournament.id_player8")

    def __init__(self, id1, id2, id3, id4, id5, id6, id7, id8):
        self.id_player1 = id1
        self.id_player2 = id2
        self.id_player3 = id3
        self.id_player4 = id4
        self.id_player5 = id5
        self.id_player6 = id6
        self.id_player7 = id7
        self.id_player8 = id8

    def __str__(self):
        if self.player_1.pts_tournament is None:
            self.player_1_pts_matchs = ""
        else:
            self.player_1_pts_matchs = f"{language.STR_PLAYER_PTS_TOURNAMENT}"\
                              f" {self.player_1.pts_tournament} " \
                              f"{language.STR_PLAYER_PTS_TOURNAMENT2}"
        if self.player_2.pts_tournament is None:
            self.player_2_pts_matchs = ""
        else:
            self.player_2_pts_matchs = f"{language.STR_PLAYER_PTS_TOURNAMENT}"\
                              f" {self.player_2.pts_tournament} " \
                              f"{language.STR_PLAYER_PTS_TOURNAMENT2}"
        if self.player_3.pts_tournament is None:
            self.player_3_pts_matchs = ""
        else:
            self.player_3_pts_matchs = f"{language.STR_PLAYER_PTS_TOURNAMENT}"\
                              f" {self.player_3.pts_tournament} " \
                              f"{language.STR_PLAYER_PTS_TOURNAMENT2}"
        if self.player_4.pts_tournament is None:
            self.player_4_pts_matchs = ""
        else:
            self.player_4_pts_matchs = f"{language.STR_PLAYER_PTS_TOURNAMENT}"\
                              f" {self.player_4.pts_tournament} " \
                              f"{language.STR_PLAYER_PTS_TOURNAMENT2}"
        if self.player_5.pts_tournament is None:
            self.player_5_pts_matchs = ""
        else:
            self.player_5_pts_matchs = f"{language.STR_PLAYER_PTS_TOURNAMENT}"\
                              f" {self.player_5.pts_tournament} " \
                              f"{language.STR_PLAYER_PTS_TOURNAMENT2}"
        if self.player_6.pts_tournament is None:
            self.player_6_pts_matchs = ""
        else:
            self.player_6_pts_matchs = f"{language.STR_PLAYER_PTS_TOURNAMENT}"\
                              f" {self.player_6.pts_tournament} " \
                              f"{language.STR_PLAYER_PTS_TOURNAMENT2}"
        if self.player_7.pts_tournament is None:
            self.player_7_pts_matchs = ""
        else:
            self.player_7_pts_matchs = f"{language.STR_PLAYER_PTS_TOURNAMENT}"\
                              f" {self.player_7.pts_tournament} " \
                              f"{language.STR_PLAYER_PTS_TOURNAMENT2}"
        if self.player_8.pts_tournament is None:
            self.player_8_pts_matchs = ""
        else:
            self.player_8_pts_matchs = f"{language.STR_PLAYER_PTS_TOURNAMENT}"\
                              f" {self.player_8.pts_tournament} " \
                              f"{language.STR_PLAYER_PTS_TOURNAMENT2}"

        return f"\n{language.STR_PLAYER_TOURNAMENT_1}" \
               f"{self.players_tournament_id} : " \
               f"\n\tID N°{self.id_player1} --- " \
               f"{self.player_1.last_name} {self.player_1.first_name} --- " \
               f"{language.STR_PLAYER_TOURNAMENT_rank}{self.player_1.rank}" \
               f"{language.STR_PLAYER_TOURNAMENT_rank2} - "\
               f"{language.STR_PLAYER_PTS_TOURNAMENT} - " \
               f"{self.player_1.pts_rank} " \
               f"{language.STR_PLAYER_PTS} - " \
               f"{self.player_1_pts_matchs}" \
               f"\n\tID N°{self.id_player2} --- " \
               f"{self.player_2.last_name} {self.player_2.first_name} --- " \
               f"{language.STR_PLAYER_TOURNAMENT_rank}{self.player_2.rank}" \
               f"{language.STR_PLAYER_TOURNAMENT_rank2} - " \
               f"{language.STR_PLAYER_PTS_TOURNAMENT} " \
               f"{self.player_2.pts_rank} " \
               f"{language.STR_PLAYER_PTS} - " \
               f"{self.player_2_pts_matchs}" \
               f"\n\tID N°{self.id_player3} --- " \
               f"{self.player_3.last_name} {self.player_3.first_name} --- " \
               f"{language.STR_PLAYER_TOURNAMENT_rank}{self.player_3.rank}" \
               f"{language.STR_PLAYER_TOURNAMENT_rank2} - " \
               f"{language.STR_PLAYER_PTS_TOURNAMENT} " \
               f"{self.player_3.pts_rank} " \
               f"{language.STR_PLAYER_PTS} - " \
               f"{self.player_3_pts_matchs}" \
               f"\n\tID N°{self.id_player4} --- " \
               f"{self.player_4.last_name} {self.player_4.first_name} --- " \
               f"{language.STR_PLAYER_TOURNAMENT_rank}{self.player_4.rank}" \
               f"{language.STR_PLAYER_TOURNAMENT_rank2} -" \
               f"{language.STR_PLAYER_PTS_TOURNAMENT} " \
               f"{self.player_4.pts_rank} " \
               f"{language.STR_PLAYER_PTS} - " \
               f"{self.player_4_pts_matchs}" \
               f"\n\tID N°{self.id_player5} --- " \
               f"{self.player_5.last_name} {self.player_5.first_name} --- " \
               f"{language.STR_PLAYER_TOURNAMENT_rank}{self.player_5.rank}" \
               f"{language.STR_PLAYER_TOURNAMENT_rank2} - " \
               f"{language.STR_PLAYER_PTS_TOURNAMENT} " \
               f"{self.player_5.pts_rank} " \
               f"{language.STR_PLAYER_PTS} - " \
               f"{self.player_5_pts_matchs}" \
               f"\n\tID N°{self.id_player6} --- " \
               f"{self.player_6.last_name} {self.player_6.first_name} --- " \
               f"{language.STR_PLAYER_TOURNAMENT_rank}{self.player_6.rank}" \
               f"{language.STR_PLAYER_TOURNAMENT_rank2} - " \
               f"{language.STR_PLAYER_PTS_TOURNAMENT} " \
               f"{self.player_6.pts_rank} " \
               f"{language.STR_PLAYER_PTS} - " \
               f"{self.player_6_pts_matchs}" \
               f"\n\tID N°{self.id_player7} --- " \
               f"{self.player_7.last_name} {self.player_7.first_name} --- " \
               f"{language.STR_PLAYER_TOURNAMENT_rank}{self.player_7.rank}" \
               f"{language.STR_PLAYER_TOURNAMENT_rank2} - " \
               f"{language.STR_PLAYER_PTS_TOURNAMENT} " \
               f"{self.player_7.pts_rank} " \
               f"{language.STR_PLAYER_PTS} - " \
               f"{self.player_7_pts_matchs}" \
               f"\n\tID N°{self.id_player8} --- " \
               f"{self.player_8.last_name} {self.player_8.first_name} --- " \
               f"{language.STR_PLAYER_TOURNAMENT_rank}{self.player_8.rank}" \
               f"{language.STR_PLAYER_TOURNAMENT_rank2} - " \
               f"{language.STR_PLAYER_PTS_TOURNAMENT} " \
               f"{self.player_8.pts_rank} " \
               f"{language.STR_PLAYER_PTS} - " \
               f"{self.player_8_pts_matchs}"


class Tournament(Base):
    __tablename__ = "T_Tournament"
    tournament_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    location = Column(String)
    date_started = Column(DateTime)
    date_finished = Column(DateTime, nullable=True)
    number_of_rounds = Column(Integer)
    time_controller = Column(String)
    description = Column(String)
    players = Column(Integer, ForeignKey(
        "T_PlayersForTournament.players_tournament_id")
                     )
    listing_players = relationship(
        "PlayersForTournament", foreign_keys="Tournament.players")
    rounds1 = Column(Integer, ForeignKey("T_Rounds.round_id"))
    rounds_details_1 = relationship(
        "Rounds", foreign_keys="Tournament.rounds1")
    rounds2 = Column(Integer, ForeignKey("T_Rounds.round_id"))
    rounds_details_2 = relationship(
        "Rounds", foreign_keys="Tournament.rounds2")
    rounds3 = Column(Integer, ForeignKey("T_Rounds.round_id"))
    rounds_details_3 = relationship(
        "Rounds", foreign_keys="Tournament.rounds3")
    rounds4 = Column(Integer, ForeignKey("T_Rounds.round_id"))
    rounds_details_4 = relationship(
        "Rounds", foreign_keys="Tournament.rounds4")

    def __init__(self, name, location, date, number_of_rounds,
                 time_controller, description):
        self.name = name
        self.location = location
        self.date_started = date
        self.number_of_rounds = number_of_rounds
        self.time_controller = time_controller
        self.description = description

    def __str__(self):
        if self.listing_players is None:
            self.listing_players_tournament = ""
        else:
            self.listing_players_tournament = self.listing_players
        if self.date_finished is None:
            self.finished = language.TOURNAMENT_NOT_END
        else:
            self.finished = self.date_finished.strftime('%d/%m/%Y %H:%M:%S')
        return f"{language.STR_TOURNAMENT_1} {self.tournament_id} : " \
               f"\n\t{language.STR_TOURNAMENT_2} {self.name}" \
               f"\n\t{language.STR_TOURNAMENT_3}" \
               f"{self.date_started.strftime('%d/%m/%Y %H:%M:%S')} " \
               f"- {self.location}" \
               f"\n\t{language.STR_TOURNAMENT_4}" \
               f"{constants.NUMBER_OF_ROUNDS} {language.STR_TOURNAMENT_5}" \
               f"\n\t{language.STR_TOURNAMENT_6} {self.time_controller} " \
               f"\n\t{language.STR_TOURNAMENT_7} {self.description} " \
               f"{self.listing_players_tournament} \n" \
               f"{language.STR_TOURNAMENT_FINISHED} {self.finished}\n"
