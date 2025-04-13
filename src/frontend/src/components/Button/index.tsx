interface Props{
    color?: string;
    onClick?: () => void;
    text?: string;
}

export default function Button({ color, onClick, text}: Props) {

    const backgroundColor = color || "bg-blue-500";

  return (
      <button 
      className={`${backgroundColor} hover:bg-blue-700 text-white font-bold py-2 px-4 rounded`}
          onClick={onClick}
      >
      {text || "Click me!"}
    </button>
  );
}