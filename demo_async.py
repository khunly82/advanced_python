import asyncio

async def main():

    async def send_mail():
        print('1. start sending email')
        await asyncio.sleep(2)
        print('3. now the email is sent')

    def huge_computation():
        str = ''
        r = 'a' * 1000
        for i in range(100_000):
            str += f'{r}{i}'
    
    loop = asyncio.get_running_loop()
    loop.run_in_executor(None, huge_computation)
    
    mail_task = asyncio.create_task(send_mail())
    await asyncio.sleep(0.1)
    print('2. before sending email something else')
    await mail_task
    print('4. after sending email i can do something else')


asyncio.run(main())