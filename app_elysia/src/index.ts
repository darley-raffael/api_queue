import { Elysia, t } from "elysia";

async function sleep(seconds: number) {
  return new Promise((resolve) => setTimeout(resolve, seconds * 1000));
}

const app = new Elysia()
  .get("/", () => "Hello Elysia")

  .post(
    "/",
    async ({ body }) => {
      await sleep(2);
      const time = Date.now().toLocaleString("pt-br");
      console.log(body.name, time);
      return {
        item: body,
      };
    },
    {
      body: t.Object({
        id: t.Number(),
        name: t.String(),
      }),
    }
  )
  .listen(3000);

console.log(
  `🦊 Elysia is running at ${app.server?.hostname}:${app.server?.port}`
);
