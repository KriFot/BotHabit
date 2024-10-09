import asyncio
import logging
from basic import main

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)#замедляет бота. отключить при выпуске
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Off')
