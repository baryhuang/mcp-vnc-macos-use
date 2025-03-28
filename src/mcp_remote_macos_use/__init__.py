import argparse
import asyncio
import logging
from . import server

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('mcp_remote_macos_use')

def main():
    logger.debug("Starting mcp_remote_macos_use main()")
    parser = argparse.ArgumentParser(description='VNC MCP Server')
    args = parser.parse_args()
    
    # Run the async main function
    logger.debug("About to run server.main()")
    asyncio.run(server.main())
    logger.debug("Server main() completed")

if __name__ == "__main__":
    main()

# Expose important items at package level
__all__ = ["main", "server"] 