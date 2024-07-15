def get_env(a):
    from dotenv import load_dotenv
    load_dotenv()
    import os
    E = os.getenv(a)
    return E
