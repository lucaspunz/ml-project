"use client";
import { Button } from "@/components/ui/button"
import { CardTitle, CardHeader, CardContent, Card } from "@/components/ui/card"
import { useState } from "react"

export function EmailSpamClassifier() {
  const [emailContent, setEmailContent] = useState<string>("")

  const [results, setResults] = useState<{logistic: number}>({logistic: 0})

  async function handleSubmit(event: React.FormEvent<HTMLFormElement>) {
    event.preventDefault()

    const response = await fetch("http://localhost:5000/predict/logistic", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ input:emailContent }),
    })
    const data = await response.json()
    setResults({
      logistic: data.logistic
    })
  }
  return (
    <section className="w-full py-12 md:py-24 lg:py-32 xl:py-48">
      <div className="container px-4 md:px-6">
        <div className="flex flex-col items-center space-y-4 text-center">
          <div className="space-y-2">
            <h1 className="text-3xl font-bold tracking-tighter sm:text-4xl md:text-5xl lg:text-6xl/none">
              Email Spam Classifier
            </h1>
            <p className="mx-auto max-w-[700px] text-zinc-500 md:text-xl dark:text-zinc-400">
              Enter the content of your email and our machine learning models will predict if it's spam or not.
            </p>
          </div>
          <div className="w-full space-y-2">
            <form className="flex flex-col space-y-2" onSubmit={handleSubmit}>
              <textarea
                aria-label="Email content"
                className="max-w-lg flex-1 h-56 p-2 border border-zinc-600/50 dark:border-zinc-500 dark:bg-zinc-700/50 rounded-md text-black dark:text-white"
                placeholder="Enter your email content"
                value={emailContent}
                onChange={(event) => setEmailContent(event.target.value)}
              />
              <Button
                className="bg-gradient-to-r from-yellow-500 via-red-500 to-purple-500 text-white hover:from-pink-500 hover:via-yellow-500 hover:to-teal-500"
                type="submit"
              >
                Analyze
              </Button>
            </form>
          </div>
        </div>
      </div>
      <div className="container px-4 md:px-6 mt-10">
        <div className="grid gap-4 lg:grid-cols-2 xl:grid-cols-3">
          <Card className="bg-gradient-to-r from-blue-500 to-green-500 text-white">
            <CardHeader>
              <CardTitle>Logistic</CardTitle>
            </CardHeader>
            <CardContent>
              <p>Spam Probability: {results.logistic*100}%</p>
            </CardContent>
          </Card>
        </div>
      </div>
    </section>
  )
}
