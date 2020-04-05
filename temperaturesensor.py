"""

OUTPUT FORMAT:
<time>,<device-id>,<region>,<temp-value>

"""

import gaussian_detector

sensorType = "temp"
gaussian_detector.start_socket(40, 30, sensorType)


