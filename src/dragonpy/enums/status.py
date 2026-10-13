# ------------------------------------------------------------------------------
# Attribution
# ------------------------------------------------------------------------------
# Portions of this module are derived from:
# https://github.com/Kludex/starlette/blob/7b2948fe7b7fff28bb018607d54cd4dfa518910e/starlette/status.py,
# Copyright (c) 2018 Encode OSS Ltd., licensed under the BSD 3-Clause License.
#
# The following license text is retained as required by the upstream license:
#
# Copyright (c) 2018, Encode OSS Ltd.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
#
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#
# * Neither the name of the copyright holder nor the names of its
#   contributors may be used to endorse or promote products derived from
#   this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ------------------------------------------------------------------------------

from enum import IntEnum


class WSSStatus(IntEnum):
    """
    WebSocket status codes.

    WebSocket codes
    ---------------
    https://www.iana.org/assignments/websocket/websocket.xml#close-code-number
    https://developer.mozilla.org/en-US/docs/Web/API/CloseEvent
    """

    WS_1000_NORMAL_CLOSURE = 1000
    WS_1001_GOING_AWAY = 1001
    WS_1002_PROTOCOL_ERROR = 1002
    WS_1003_UNSUPPORTED_DATA = 1003
    WS_1005_NO_STATUS_RCVD = 1005
    WS_1006_ABNORMAL_CLOSURE = 1006
    WS_1007_INVALID_FRAME_PAYLOAD_DATA = 1007
    WS_1008_POLICY_VIOLATION = 1008
    WS_1009_MESSAGE_TOO_BIG = 1009
    WS_1010_MANDATORY_EXT = 1010
    WS_1011_INTERNAL_ERROR = 1011
    WS_1012_SERVICE_RESTART = 1012
    WS_1013_TRY_AGAIN_LATER = 1013
    WS_1014_BAD_GATEWAY = 1014
    WS_1015_TLS_HANDSHAKE = 1015
