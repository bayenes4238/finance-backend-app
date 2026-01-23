import yahooFinance from "yahoo-finance2";
import fs from "fs-extra";

const BIST = {
  THYAO: "THYAO.IS",
  ASELS: "ASELS.IS",
  KCHOL: "KCHOL.IS"
};

const US = {
  AAPL: "AAPL",
  MSFT: "MSFT",
  TSLA: "TSLA",
  NVDA: "NVDA"
};

async function fetchGroup(map) {
  const out = {};
  for (const key in map) {
    try {
      const q = await yahooFinance.quote(map[key]);
      out[key] = {
        p: Number(q.regularMarketPrice.toFixed(2)),
        c: Number(q.regularMarketChangePercent.toFixed(2))
      };
    } catch {
      out[key] = { p: 0, c: 0 };
    }
  }
  return out;
}

async function main() {
  const data = {
    stocks: {
      bist: await fetchGroup(BIST),
      us: await fetchGroup(US)
    },
    ts: Math.floor(Date.now() / 1000)
  };

  await fs.writeJson("data.json", data);
}

main();
