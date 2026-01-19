// example of code to parse
// let variable = mod(10);


enum TokenType {
    Let, //how to manage this?
    Identifier, //how to manage this?
    Number, //how to manage this?
    Keyword, //how to manage this?
    OpenParenthesis,
    ClosingParenthesis,
    Semicolon,
}

interface Token {
    type: TokenType,
    value: string
}

// change value to be a correspondig set of defined mapped keys
function buildToken(type: TokenType, value: string): Token {
    return {type: type, value: value} 
}

export function tokenize(source: string): Token[] {
    let src = source.split(""); //all the chars 
    let tokens: Token[] = [];
    
    while (src.length > 0) {
        
        switch (src[0]){ //always the first element (because we shift everything)
        
            case "(":
                tokens.push(buildToken(
                    TokenType.OpenParenthesis, 
                    src.shift()
                ));
                break;

            case ")":
                tokens.push(buildToken(
                    TokenType.ClosingParenthesis, 
                    src.shift()
                ));
                break;

            case ";":
                tokens.push(buildToken(
                    TokenType.Semicolon, 
                    src.shift()
                ));
                break;

            default: //all unmanaged tokens
                tokens.push(buildToken(
                    TokenType.Semicolon, 
                    src.shift()
                ));
                break;
        
        } 
            

    }

    return tokens
}
