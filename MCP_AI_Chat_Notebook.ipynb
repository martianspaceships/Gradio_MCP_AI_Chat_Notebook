import asyncio
from contextlib import AsyncExitStack
from mcp.client.sse import sse_client
from mcp import ClientSession
from rich.console import Console
from rich.markdown import Markdown
from typing import Optional

# Import the ollama library
import ollama

# This is often needed in Jupyter to run asyncio loops
import nest_asyncio
nest_asyncio.apply()

# --- Configuration ---
# Set your Gradio MCP server URL and the Ollama model (typically "http://localhost:7860/gradio_api/mcp/sse"): 
GRADIO_MCP_SERVER_URL = "Use_your_MCP_server_URL_here"
OLLAMA_MODEL = "llama3.1:8b"  # update to model you want to use

# --- MCP Client Class ---
class GradioMCPClient:
    """
    A client for connecting to a Gradio-based MCP server from a Jupyter Notebook.
    It handles tool calling with Ollama.

    This class is an asynchronous context manager. The `connect` and
    `cleanup` logic are handled by the `__aenter__` and `__aexit__` methods.
    """

    def __init__(self, model: str = OLLAMA_MODEL):
        """
        Initializes the client with the specified Ollama model.
        """
        self.console = Console()
        self.model = model
        self.session: Optional[ClientSession] = None
        self.ollama = None
        self._exit_stack: Optional[AsyncExitStack] = None

    async def __aenter__(self):
        """
        Entry point for the async context manager. Handles connection logic
        with retry and timeout.
        """
        max_retries = 5
        base_delay = 1.0  # seconds
        connect_timeout = 30.0  # Increased timeout for server init

        self.console.print(f"[bold cyan]Attempting to connect to Gradio MCP server at {GRADIO_MCP_SERVER_URL} with a {connect_timeout}-second timeout...[/bold cyan]")

        for attempt in range(1, max_retries + 1):
            try:
                self.console.print(f"[dim]Attempt {attempt}/{max_retries}: Initializing Ollama client...[/dim]")
                self.ollama = ollama.AsyncClient()

                self.console.print("[dim]Creating SSE client streams and MCP session...[/dim]")
                self._exit_stack = AsyncExitStack()

                streams = await self._exit_stack.enter_async_context(
                    sse_client(GRADIO_MCP_SERVER_URL)
                )

                self.session = await self._exit_stack.enter_async_context(
                    ClientSession(*streams)
                )

                self.console.print("[dim green]SSE client streams and MCP session successfully created.[/dim green]")

                self.console.print("[dim]Initializing MCP session...[/dim]")
                await asyncio.wait_for(self.session.initialize(), timeout=connect_timeout)

                meta = await self.session.list_tools()
                self.console.print("Server connected successfully!", style="bold green")
                self.console.print("Available tools:", [t.name for t in meta.tools], style="dim green")
                return self  # Return the client instance

            except asyncio.TimeoutError:
                self.console.print(f"[bold red]Attempt {attempt}/{max_retries}: Connection timed out after {connect_timeout} seconds. The server may be taking a long time to start up.[/bold red]")
            except Exception as e:
                self.console.print(f"Attempt {attempt}/{max_retries}: Failed to connect due to: [bold red]{e}[/bold red]")

            if attempt < max_retries:
                delay = base_delay * (2 ** (attempt - 1))
                self.console.print(f"[dim]Retrying in {delay:.1f} seconds...[/dim]")
                await asyncio.sleep(delay)

        self.console.print("[bold red]Failed to connect after multiple retries. Please ensure the Gradio server is running and accessible.[/bold red]")
        raise RuntimeError("Failed to connect to Gradio server.")

    async def __aexit__(self, exc_type, exc_value, traceback):
        """
        Exit point for the async context manager. Handles cleanup logic.
        """
        self.console.print("[dim]Cleaning up client resources...[/dim]")
        try:
            # If using an older ollama AsyncClient version that supports explicit closing,
            # you could uncomment the next line:
            # await self.ollama.aclose()

            if self._exit_stack:
                await self._exit_stack.aclose()
                self._exit_stack = None
            self.session = None
            self.console.print("[dim]Client cleaned up successfully.[/dim]")
        except Exception as e:
            self.console.print(f"An error occurred during cleanup: [bold red]{e}[/bold red]")

    async def query(self, user_query: str):
        """
        Processes a single user query by interacting with Ollama and the MCP server.

        Args:
            user_query (str): The query from the user.
        """
        if not self.session:
            self.console.print("[bold red]Client not connected. Please use the client with 'async with' and ensure the connection is successful.[/bold red]")
            return

        self.console.print(f"[bold blue]Query:[/bold blue] {user_query}")

        try:
            messages = [{"role": "user", "content": user_query}]
            meta = await self.session.list_tools()
            tools_meta = [{"type": "function", "function": {"name": t.name, "description": t.description, "parameters": t.inputSchema}} for t in meta.tools]

            resp = await self.ollama.chat(model=self.model, messages=messages, tools=tools_meta)

            final_response = []

            if getattr(resp.message, "content", None):
                final_response.append(resp.message.content)
            elif resp.message.tool_calls:
                for tc in resp.message.tool_calls:
                    self.console.print(f"[dim yellow]Calling tool '{tc.function.name}' with arguments: {tc.function.arguments}[/dim yellow]")
                    result = await self.session.call_tool(tc.function.name, tc.function.arguments)

                    messages.append({"role": "tool", "name": tc.function.name, "content": result.content[0].text})

                    resp = await self.ollama.chat(model=self.model, messages=messages, tools=tools_meta, options={"max_tokens": 500})
                    final_response.append(resp.message.content)

            self.console.print(Markdown("".join(final_response), style="orange3"))

        except Exception as e:
            self.console.print(f"An error occurred during query processing: [bold red]{e}[/bold red]")


async def main():
    """
    Main function to run the client in a conversational loop.
    It prompts the user for input, queries the client, and repeats until 'quit' is typed.
    """
    async with GradioMCPClient() as client:
        while True:
            user_input = input("What would you like to know? (or type 'quit' to exit): ")
            if user_input.lower() == 'quit':
                break
            await client.query(user_input)

if __name__ == "__main__":
    asyncio.run(main())
