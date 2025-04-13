"use client";


import Button from "@/components/Button";
import styles from "./styles.module.css"

export default function Products() {

    function handleClick() {
        alert("Bom dia");
    }

  return (
      <div className={styles.title}>
      <h1>
        <span className="text-6xl font-bold text-center text-white">
          Products page
        </span>
        <br />
        <span className="text-2xl font-bold text-center text-white">
          This is a simple Next.js app with Tailwind CSS and TypeScript.
        </span>
              <Button color="bg-gray-500" text="Cadastrar" onClick={handleClick}/>
      </h1>
    </div>
  );
}