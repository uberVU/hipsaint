#!/usr/bin/env python
from optparse import OptionParser
import hipsaint
from ..messages import HipchatMessage


def main():
    usage = "Usage: %prog [options] [action]..."

    parser = OptionParser(usage, version="%%prog v%s" % hipsaint.__version__)

    parser.add_option("-r", "--room",
                      dest="room_id",
                      default="",
                      help="HipChat room id deliver message to")

    parser.add_option("-u", "--user",
                      dest="user",
                      default="Nagios",
                      help="Username to deliver message as")

    parser.add_option("-t", "--token",
                      dest="token",
                      default="",
                      help="HipChat API token to use")

    parser.add_option("-i", "--inputs",
                      dest="inputs",
                      default="",
                      help="Input variables from Nagios separated by |")

    parser.add_option("-T", "--type",
                      dest="msg_type",
                      default="",
                      help="Mark if notification is from host group or service group, "
                           "host|service|short-host|short-service")

    parser.add_option("-n", "--notify",
                      action="store_true",
                      default=False,
                      dest="notify",
                      help="Whether or not this message should trigger a "
                           "notification for people in the room")

    ### Parse command line
    (options, args) = parser.parse_args()
    ### Validate required input
    if not options.token:
        parser.error('--token is required')
    if not options.inputs:
        parser.error('--inputs is required')
    if not options.room_id:
        parser.error('--room is required')
    if not options.msg_type:
        parser.error('--type is required')
    msg = HipchatMessage(**vars(options))
    msg.deliver_payload()


if __name__ == "__main__":
    main()
