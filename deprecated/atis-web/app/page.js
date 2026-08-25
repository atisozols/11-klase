import ClickCounter from "@/components/ClickCounter";
import Collapsible from "@/components/Collapsible";
import ColorChangingButton from "@/components/ColorChangingButton";
import HelloWorld from "@/components/HelloWorld";
import Profile from "@/components/Profile";
import Link from "next/link";

export default function Home() {
  return (
    <div>
      <HelloWorld message={"This is a passed message"} />
      <Profile name="Atis" isMorning={true} />
      <ClickCounter initial={100} />
      <Collapsible />
      <ColorChangingButton />
      <Link href={"/blog"}>Uz blog sadaļu</Link>
      <a href="https://www.e-klase.lv">Uz e-klase</a>
    </div>
  );
}
