from typing import Any, Callable


class ToolRegistry:
    """Contrat de registre MCP ; protocole et logique privés non inclus."""

    def register(self, name: str, tool: Callable[..., Any]) -> None:
        # logique privée — non incluse
        raise NotImplementedError("logique privée — non incluse")

    def list_tools(self) -> list[str]:
        # logique privée — non incluse
        raise NotImplementedError("logique privée — non incluse")

    def call(self, name: str, arguments: dict[str, Any]) -> Any:
        # logique privée — non incluse
        raise NotImplementedError("logique privée — non incluse")
