from abc import ABC, abstractmethod


class Agent(ABC):
    @abstractmethod
    def run(self) -> None:
        # logique privée — non incluse
        raise NotImplementedError("logique privée — non incluse")
