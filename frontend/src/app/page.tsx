import Image from "next/image";
import { EmailSpamClassifier } from "../components/email-spam-classifier";

export default function Home() {
  return (
    <main>
      <EmailSpamClassifier />
    </main>
  );
}
