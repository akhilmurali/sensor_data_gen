"""
For Official Documentation and More Information Refer
https://docs.python.org/3/library/socket.html

OUTPUT FORMAT:
<time>,<device-id>,<region>,<smoke>

"""
import binary_detector
LIMIT = 0.6
binary_detector.start_socket(LIMIT)

