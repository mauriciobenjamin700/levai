export default function Home() {
  return (
    <div className="grid grid-rows-[20px_1fr_20px] items-center justify-items-center min-h-screen p-8 pb-20 gap-16 sm:p-20 font-[family-name:var(--font-geist-sans)]">
      <h1>
        <span className="text-6xl font-bold text-center text-white">
          Hello World!
        </span>
        <br />
        <span className="text-2xl font-bold text-center text-white">
          This is a simple Next.js app with Tailwind CSS and TypeScript.
        </span>
      </h1>
    </div>
  );
}
