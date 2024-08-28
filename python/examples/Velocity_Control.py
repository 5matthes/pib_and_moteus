import asyncio
import math
import moteus
import moteus.moteus_tool as mt

async def main():
    # By default, Controller connects to id 1, and picks an arbitrary
    # CAN-FD transport, prefering an attached fdcanusb if available.
    c = moteus.Controller()
    s = moteus.Stream(c)
    print("1111")
    #d = mt.Stream(c, "1", "None")

    # In case the controller had faulted previously, at the start of
    # this script we send the stop command in order to clear it.
    await c.set_stop()
    print("2")

    #state = await c.set_position(position=math.nan, query=True)
    #stop_position: Currently not understood, but with a value it's not moving
    #velocity_limit: not persisted in controller
    await s.command(b"conf set servopos.position_min NaN")
    print("3")
    await s.command(b"conf set servopos.position_max NaN")
    print("4")
    state = await c.set_position(position=math.nan, query=True)
    print(state)

    # Print out just the position register.
    print("Position:", state.values[moteus.Register.POSITION])
    state = await c.set_position(position=-4, velocity_limit=0.5, accel_limit=5.0,stop_position = math.nan, watchdog_timeout=math.nan, query=True)
    await asyncio.sleep(5)
    # Print out everything.
    print(state)

    # Print out just the position register.
    print("Position:", state.values[moteus.Register.POSITION])
    state = await c.set_position(position=12, velocity = 4.0, watchdog_timeout=12, query=True)
    
    # Print out everything.
    print(state)

    # Print out just the position register.
    print("Position:", state.values[moteus.Register.POSITION])

    await asyncio.sleep(5)


if __name__ == '__main__':
    asyncio.run(main())