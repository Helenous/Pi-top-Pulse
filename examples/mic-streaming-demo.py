#!/usr/bin/env python

"""
MIT License

Copyright (c) 2017 CEED Ltd.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Basic example showing how the record_async
generator(https://wiki.python.org/moin/Generators) function can be used to
stream data from the microphone in realtime. In this example the function is
used to produce a vertically scrolling audio level indicator.  
"""

import statistics
from ptpulse import microphone

microphone.set_sample_rate_to_16khz()
microphone.set_bit_rate_to_signed_16()

audio_generator = microphone.record_async()
sample = bytearray()
for data in audio_generator:
    if len(sample) < 4000:
        sample += data
    else:
        average = statistics.mean(sample)
        print((average/255) * 100)
        sample = []
