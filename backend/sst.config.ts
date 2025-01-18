/// <reference path="./.sst/platform/config.d.ts" />

export default $config({
  app(input) {
    return {
      name: "amp-alert",
      removal: input?.stage === "production" ? "retain" : "remove",
      protect: ["production"].includes(input?.stage),
      home: "aws",
    };
  },
  async run() {
    const backend = new sst.aws.Function("Backend", {
      handler: "function/main.handler",
      runtime: "python3.12",
      url: true,
      python: { container: true },
    });
  },
});
