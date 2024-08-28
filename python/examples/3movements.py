#!/usr/bin/python3 -B

# Copyright 2023 mjbots Robotic Systems, LLC.  info@mjbots.com
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


"""
This example commands a single servo at ID #1 using the default
transport to hold the current position indefinitely, and prints the
state of the servo to the console.
"""

import asyncio
import math
import moteus

async def main():
    # By default, Controller connects to id 1, and picks an arbitrary
    # CAN-FD transport, prefering an attached fdcanusb if available.
    c = moteus.Controller()

    # In case the controller had faulted previously, at the start of
    # this script we send the stop command in order to clear it.
    await c.set_stop()

    #state = await c.set_position(position=math.nan, query=True)
    #state = await c.set_position(position=0.0, velocity_limit=0.5, accel_limit=5.0, watchdog_timeout=math.nan, query=True)
    state = await c.set_position(position=-0.2, query=True)
    # Print out everything.
    print(state)

    # Print out just the position register.
    print("Position:", state.values[moteus.Register.POSITION])

    # And a blank line so we can separate one iteration from the
    # next.
    print()

    # Wait 20ms between iterations.  By default, when commanded
    # over CAN, there is a watchdog which requires commands to be
    # sent at least every 100ms or the controller will enter a
    # latched fault state.
    await asyncio.sleep(1)

    ##########################

    #state = await c.set_position(position=-0.4, velocity=2, maximum_torque=1, feedforward_torque=1,kp_scale=1,kd_scale=1, query=True)

    # Print out everything.
    print(state)

    # Print out just the position register.
    print("Position:", state.values[moteus.Register.POSITION])

    # And a blank line so we can separate one iteration from the
    # next.
    print()

    # Wait 20ms between iterations.  By default, when commanded
    # over CAN, there is a watchdog which requires commands to be
    # sent at least every 100ms or the controller will enter a
    # latched fault state.
    await asyncio.sleep(1)

    #state = await c.set_position(position=0, velocity=2, maximum_torque=1, feedforward_torque=1,kp_scale=1,kd_scale=1, query=True)
    # Print out everything.
    print(state)

    # Print out just the position register.
    print("Position:", state.values[moteus.Register.POSITION])

    # And a blank line so we can separate one iteration from the
    # next.
    print()

    # Wait 20ms between iterations.  By default, when commanded
    # over CAN, there is a watchdog which requires commands to be
    # sent at least every 100ms or the controller will enter a
    # latched fault state.
    await asyncio.sleep(1)

    #state = await c.set_position(position=0.45, velocity=2, maximum_torque=1, feedforward_torque=1,kp_scale=1,kd_scale=1, query=True)

    # Print out everything.
    print(state)

    # Print out just the position register.
    print("Position:", state.values[moteus.Register.POSITION])

    # And a blank line so we can separate one iteration from the
    # next.
    print()

    # Wait 20ms between iterations.  By default, when commanded
    # over CAN, there is a watchdog which requires commands to be
    # sent at least every 100ms or the controller will enter a
    # latched fault state.
    await asyncio.sleep(1)

    

    # Print out everything.
    print(state)

    # Print out just the position register.
    print("Position:", state.values[moteus.Register.POSITION])

    # And a blank line so we can separate one iteration from the
    # next.
    print()

    # Wait 20ms between iterations.  By default, when commanded
    # over CAN, there is a watchdog which requires commands to be
    # sent at least every 100ms or the controller will enter a
    # latched fault state.
    await asyncio.sleep(0.5)





if __name__ == '__main__':
    asyncio.run(main())
