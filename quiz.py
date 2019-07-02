from cryptography.fernet import Fernet

key = 'TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM='

# Oh no! The code is going over the edge! What are you going to do?
message = b'gAAAAABdBNbUgCGa22RaFQfWODcoZedXDuZLrRvAeU17MbR3T2kb6zhunxHVsY2JusJXUULM1YEjGKV8AGpNNW_-E49qZ4jNk3yu7zKwL8tiQLUsUW5hqlVMwkm8m1QP8zntgOHCwzuocqcwQxjPlWPvFfdkV5AwMqqj7fSx-EHk2agZ0pqBpIY='

def main():
    f = Fernet(key)
    print(f.decrypt(message))


if __name__ == "__main__":
    main()
