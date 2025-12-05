require("@nomiclabs/hardhat-ethers");
require('dotenv').config();

module.exports = {
  solidity: "0.8.17",
  networks: {
    // Fill RPC URL and private key in .env when you deploy:
    // SEPOLIA_URL and PRIVATE_KEY
    sepolia: {
      url: process.env.SEPOLIA_URL || "",
      accounts: process.env.PRIVATE_KEY ? [process.env.PRIVATE_KEY] : []
    }
  }
};