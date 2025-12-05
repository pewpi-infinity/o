async function main() {
  const [deployer] = await ethers.getSigners();
  console.log("Deploying contracts with account:", deployer.address);

  const name = process.env.TOKEN_NAME || "ResearchToken";
  const symbol = process.env.TOKEN_SYMBOL || "RSD";
  const initialMinter = process.env.INITIAL_MINTER || deployer.address;

  const ERC20Mintable = await ethers.getContractFactory("ERC20Mintable");
  const token = await ERC20Mintable.deploy(name, symbol, initialMinter);
  await token.deployed();
  console.log("ERC20Mintable deployed to:", token.address);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});