from digs.messaging.serialization import Serializable
from digs.messaging.actions import Action


class HeartBeat(Action):
    __action__ = 'heartbeat'

    time = int


class Error(Action):
    __action__ = 'error'

    kind = str
    message = str


class Announce(Action):
    __action__ = 'announce'

    hostname = str
    type = str


class Job(Serializable):
    program_name = str


class JobRequest(Action):
    __action__ = 'job_request'

    job = Job


class PerformJob(Action):
    __action__ = 'perform_job'

    job = Job


class LocateData(Action):
    __action__ = 'locate_data'

    filenames = list
