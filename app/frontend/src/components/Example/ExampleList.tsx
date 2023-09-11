import { Example } from "./Example";

import styles from "./Example.module.css";

export type ExampleModel = {
    text: string;
    value: string;
};

const EXAMPLES: ExampleModel[] = [
    {
        text: "How to pair the wireless scan gun to the tablet?",
        value: "How to pair the wireless scan gun to the tablet?"
    },
    {
        text: "How to print from HIBBNET?",
        value: "How to print from HIBBNET?"
    },
    {
        text: "How do I access store survey?",
        value: "How do I access store survey?"
    }
];

interface Props {
    onExampleClicked: (value: string) => void;
}

export const ExampleList = ({ onExampleClicked }: Props) => {
    return (
        <ul className={styles.examplesNavList}>
            {EXAMPLES.map((x, i) => (
                <li key={i}>
                    <Example text={x.text} value={x.value} onClick={onExampleClicked} />
                </li>
            ))}
        </ul>
    );
};
