import 'dotenv/config';
import OpenAI from "openai";
const client = new OpenAI();

const response = await client.responses.create({
    model: "gpt-5.4-mini",
    input: "Write a one-sentence bedtime about the start of a interaction between a kid  and an AI.",
    stream:true
});
//gives  back a delta of the answer  
for await (const event of response) {
  if (event.type === "response.output_text.delta") {
    process.stdout.write(event.delta);
  }
}
// this does not exist in stream true console.log(response.output_text);

//then the chat behavior 
let messages=[
    {role:"system",content:"you are a very helpful  assistant",
        role:"user",content:"what was the name of the machines that had all information on the halo in Halo saga?"
    }
];
const response1=await client.chat.completions.create(
    {model:"gpt-5.4-mini",
        messages
        //n: a number  will give you that  number of  responses for the same question under ther choices  array 
    }
);

console.log(response1.choices[0].message.content);
messages = messages.concat([response1.choices[0].message]);
messages.push({ role: "user", content: "and their function ?" });

const response2 = await client.chat.completions.create({
  model: "gpt-5.4-mini",
  messages,
});

console.log(response2.choices[0].message.content);
// now  the while loop 
import readline from "readline/promises";
const rl = readline.createInterface({ input: process.stdin, output: process.stdout });

const messages = [{ role: "system", content: "Eres un asistente útil" }];

while (true) {
  const userInput = await rl.question("You: ");
  if (userInput === "exit") break;

  messages.push({ role: "user", content: userInput });

  const res = await client.chat.completions.create({
    model: "gpt-5.4-mini",
    messages,
  });

  const reply = res.choices[0].message;
  messages.push(reply);
  console.log("AI:", reply.content);
}
rl.close();