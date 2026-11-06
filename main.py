import time

class TokenBucket:
    def __init__(self, capacity: int, refill_rate: float):
        self.capacity = capacity
        self.refill_rate = refill_rate
        self.tokens = capacity
        self.last_refill = time.time()

    def consume(self, amount: int = 1) -> bool:
        now = time.time()
        elapsed = now - self.last_refill
        self.tokens = min(self.capacity, self.tokens + elapsed * self.refill_rate)
        self.last_refill = now
        if self.tokens >= amount:
            self.tokens -= amount
            return True
        return False

if __name__ == '__main__':
    bucket = TokenBucket(capacity=5, refill_rate=1.0)
    assert bucket.consume(3) is True
    assert bucket.consume(2) is True
    assert bucket.consume(1) is False
    print("Token Bucket Rate Limiter OK")
